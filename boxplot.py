import csv
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        for row in reader:
            for value in row:
                try:
                    data.append(float(value))  # Attempt to convert each entry to float
                except ValueError:
                    continue  # Skip non-numeric values
    return data

def calculate_five_number_summary(data):
    if not data:
        return None, None, None, None, None
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    def median(data):
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]
    
    min_val = sorted_data[0]
    q1 = median(sorted_data[:n // 2])
    q3 = median(sorted_data[(n + 1) // 2:])
    med = median(sorted_data)
    max_val = sorted_data[-1]
    
    return min_val, q1, med, q3, max_val

def plot_boxplot(five_number_summary):
    if any(x is None for x in five_number_summary):
        print("Data is not sufficient to plot the boxplot.")
        return
    
    min_val, q1, med, q3, max_val = five_number_summary

    # Create a ColumnDataSource for Bokeh
    source = ColumnDataSource(data=dict(
        q=[med],
        q1=[q1],
        q3=[q3],
        min=[min_val],
        max=[max_val]
    ))

    # Create a figure
    p = figure(title="Boxplot of Five-Number Summary", plot_height=250, plot_width=600, y_range=["Boxplot"])

    # Add the boxplot
    p.segment(x0=0, x1=0, y0=min_val, y1=max_val, line_width=2, line_color="blue")
    p.vbar(x=0, width=0.2, bottom=q1, top=q3, fill_color="lightblue", line_color="blue")
    p.line(x=[0.1, 0.3], y=[med, med], line_width=2, line_color="red")

    p.yaxis.axis_label = "Value"
    p.xaxis.axis_label = ""
    p.xaxis.visible = False

    # Show plot
    output_file("boxplot.html")
    show(p)

# Main script
filename = 'Sales_Transactions.csv'  # Replace with your CSV file path
data = read_csv(filename)
five_number_summary = calculate_five_number_summary(data)
plot_boxplot(five_number_summary)
