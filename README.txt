Basic Access Control Mechanism

Guide:
- Use this repository or simply have the "portal.py" file in a folder
- Use the command line to run any of the 8 access controls
- Follow the example inputs below
- If you receive an error change "python" to "python3"
- Text files will be created and updated depending on your input

Example Command Line Inputs:

AddUser:

    python portal.py AddUser user1 password1


Authenticate:

    python portal.py Authenticate user1 password1


SetDomain:

    python portal.py SetDomain user1 basic_users


DomainInfo:

    python portal.py DomainInfo basic_users


SetType:

    python portal.py SetType basketball sports


TypeInfo:

    python portal.py TypeInfo sports


AddAccess:

    python portal.py AddAccess play basic_users sports


CanAccess:

    python portal.py CanAccess play user1 basketball

