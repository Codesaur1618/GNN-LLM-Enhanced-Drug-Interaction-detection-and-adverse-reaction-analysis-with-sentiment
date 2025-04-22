import xml.etree.ElementTree as ET
import csv

def xml_to_csv(xml_file, csv_file):
    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Define a header based on your XML structure
        # Example: ['Column1', 'Column2', 'Column3']
        csv_writer.writerow(['Column1', 'Column2', 'Column3'])  # Adjust headers as needed

        # Parse the XML file
        for event, elem in ET.iterparse(xml_file, events=('end',)):
            if elem.tag == 'YourElement':  # Adjust to your XML element
                # Extract data from the XML element
                column1 = elem.find('SubElement1').text if elem.find('SubElement1') is not None else ''
                column2 = elem.find('SubElement2').text if elem.find('SubElement2') is not None else ''
                column3 = elem.find('SubElement3').text if elem.find('SubElement3') is not None else ''
                
                # Write the extracted data to the CSV file
                csv_writer.writerow([column1, column2, column3])
                
                # Clear the element to save memory
                elem.clear()

# Example usage
xml_to_csv("C:/Users/abise/Downloads/faers_xml_2024q2/XML/1_ADR24Q2.xml", 'C:/Users/abise/Downloads/faers_xml_2024q2/XML/1_output_file.csv')
