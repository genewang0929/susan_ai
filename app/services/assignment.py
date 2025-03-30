from ..schemas.assignment import Assignment
import xml.etree.ElementTree as ET

async def get_all_assignment_info():
    assignment_data = [
        Assignment(claim_number='WD-2025-1234', policy_number="Assignment 1", loss_date='2025-03-15', insured_id='1'),
        Assignment(claim_number='WD-2025-1235', policy_number="Assignment 2", loss_date='2025-03-16', insured_id='2'),
        Assignment(claim_number='WD-2025-1236', policy_number="Assignment 3", loss_date='2025-03-17', insured_id='3'),
        Assignment(claim_number='WD-2025-1237', policy_number="Assignment 4", loss_date='2025-03-18', insured_id='4'),
    ]

    return assignment_data

# def parse_xml():
    tree = ET.parse('sample.xml')
    root = tree.getroot()
    for child in root.findall("./ASSIGNMENT/"):
        print(child.tag, child.text)
    # assignment = root[0]
    # insured = assignment[3]
    # address = insured[1]
    # for child in address:
    #     print(child.tag, child.text)

    # estimates = root[1]
    # line_items = estimates[0]
    # for item in line_items:
    #     for child in item:
    #         print(child.tag, child.text)
    # rooms = estimates[1]
    # for room in rooms:
    #     for child in room:
    #         print(child.tag, child.text)

async def insert_assignment(assignment_str):
    root = ET.fromstring(assignment_str)
    for child in root.findall("./ASSIGNMENT/"):
        print(child.tag, child.text)
    # assignment = root[0]
    # insured = assignment[3]
    # address = insured[1]
    # for child in address:
    #     print(child.tag, child.text)

    # estimates = root[1]
    # line_items = estimates[0]
    # for item in line_items:
    #     for child in item:
    #         print(child.tag, child.text)
    # rooms = estimates[1]
    # for room in rooms:
    #     for child in room:
    #         print(child.tag, child.text)

    # return assignment
