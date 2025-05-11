import os
import re


questionSegment = "File and Print Server"

questions = """
1. What is a file server, and what is its primary function in a network?
2. Explain the role of a print server and how it operates within a network.
3. How do file servers manage access to shared resources?
4. What are common protocols used by file servers to share files across a network?
5. How does a file server ensure data integrity and security?
6. What is the difference between a file server and a database server?
7. Describe how file permissions are managed on a file server.
8. What are the benefits of using a centralized file server for an organization?
9. Explain how a print server handles print jobs from multiple clients.
10. What are common security risks associated with file servers, and how can they be mitigated?
11. How can you configure file sharing on a file server using the SMB protocol?
12. What role does a print server play in managing printer drivers and configurations?
13. How do you monitor and manage storage usage on a file server?
14. What is the difference between a local print server and a network print server?
15. How does a file server support backups and disaster recovery strategies?
16. What steps would you take to troubleshoot a print server that is not processing print jobs?
17. What is the importance of access control lists (ACLs) on file servers?
18. How can print quotas be enforced on a print server to manage printer resources?
19. What is the process for adding a new printer to a print server in a Windows environment?
20. How does a file server ensure high availability and redundancy in an enterprise network?
"""

answers = """
1. A file server is a computer or device that provides centralized storage and management of files. Its primary
function is to allow multiple users on a network to access and share files securely.
2. A print server manages and directs print jobs from multiple computers to one or more printers. It queues
print jobs, manages printer drivers, and ensures that printing is handled efficiently within a network.
3. File servers manage access to shared resources by using permissions and authentication mechanisms.
These can include setting up user accounts, groups, and defining who has read, write, or modify access to
specific files or directories.
4. Common protocols used by file servers include SMB (Server Message Block), NFS (Network File System),
and FTP (File Transfer Protocol). These protocols allow users to access, transfer, and manage files over a
network.
5. A file server ensures data integrity and security by implementing access controls, encryption, and regular
backups. Permissions limit access to files, and encryption can protect the data during transmission.
6. A file server primarily stores and manages file-based data, whereas a database server stores and manages
structured data in databases. The database server is optimized for complex queries and transaction
management, while a file server handles unstructured data like documents and media.
7. File permissions on a file server are managed through access control lists (ACLs), which specify the level of
access users and groups have over files and folders. These permissions can be set to allow or deny actions
like reading, writing, or modifying files.
8. The benefits of using a centralized file server include easier management of data, improved collaboration,
better security controls, and more efficient backup and disaster recovery processes. Centralization also
simplifies network administration.
9. A print server queues print jobs from multiple clients, prioritizes them, and sends them to the designated
printers. It manages the distribution of print jobs and ensures that each print job is processed in the
correct order without conflicts.
10. Common security risks for file servers include unauthorized access, data breaches, malware attacks, and
data loss. These risks can be mitigated by implementing strong access controls, encryption, regular
security updates, and robust backup solutions.
11. File sharing can be configured on a file server using the SMB protocol by enabling file sharing services and
assigning shared folders with appropriate permissions. This is typically done through the server's operating
system or management interface.
12. A print server manages printer drivers by ensuring that each connected client has the correct driver
installed. It also handles printer configurations, allowing centralized control over printer settings and
resources.
13. Storage usage on a file server can be monitored and managed by tracking disk space usage, setting storage
quotas, and using file management tools to identify large or unused files. Administrators may also
configure alerts for storage limits.
14. A local print server is directly attached to a printer and serves print jobs from one or more local devices,
while a network print server connects printers to the entire network. A network print server allows multiple
clients to access and share printers over the network.
15. A file server supports backups and disaster recovery by regularly copying files to a secure backup system.
Redundant configurations, such as RAID, can also protect against data loss by duplicating data across
multiple drives.
16. To troubleshoot a print server that is not processing jobs, you would check the print queue for errors, verify
network connectivity, restart the print spooler service, ensure that the correct drivers are installed, and
verify that the printer is online.
17. Access control lists (ACLs) on file servers define which users or groups can access certain files or
directories and what actions they can perform. ACLs are essential for ensuring that only authorized
personnel can access sensitive data.
18. Print quotas can be enforced on a print server by configuring settings that limit the number of pages or print
jobs a user or group can print. This helps manage resources and control printing costs.
19. Adding a new printer to a print server in a Windows environment involves installing the appropriate printer
driver, configuring the printer’s IP address, and sharing it with the network. The printer can then be added
to the server via the Devices and Printers settings.
20. A file server ensures high availability and redundancy through techniques such as clustering, RAID
configurations, and load balancing. Redundancy ensures that if one server fails, another can take over
without disruption.
"""


filePathQuestion = fr"/home/jack/Desktop/Programming Projects/Cyber Op Question Bank/asset/{questionSegment}/Questions"
filePathAnswer = fr"/home/jack/Desktop/Programming Projects/Cyber Op Question Bank/asset/{questionSegment}/Answers"

os.makedirs(filePathQuestion, exist_ok=True)
os.makedirs(filePathAnswer, exist_ok=True)





#QUESTIONS
linesQuestions = questions.strip().splitlines()
mergedQuestions = ""
for line in linesQuestions:
    if re.match(r"^\d+\.\s", line):
        mergedQuestions += "\n" + line  # Start a new question
    else:
        mergedQuestions += " " + line.strip()  # Continue the current line

matchesQuestions = re.findall(r"(\d+)\.\s+(.*?)(?=\n\d+\.|\Z)", mergedQuestions, re.DOTALL)

for num, content in matchesQuestions:
    filename = os.path.join(filePathQuestion, f"Question{num}.txt")
    
    with open(filename, "w") as file:
        file.write(content.strip())


#ANSWERS
linesAnswers = answers.strip().splitlines()
mergedAnswers = ""
for line in linesAnswers:
    if re.match(r"^\d+\.\s", line):
        mergedAnswers += "\n" + line  # Start a new question
    else:
        mergedAnswers += " " + line.strip()  # Continue the current line

matchesAnswers = re.findall(r"(\d+)\.\s+(.*?)(?=\n\d+\.|\Z)", mergedAnswers, re.DOTALL)

for num, content in matchesAnswers:
    filename = os.path.join(filePathAnswer, f"Answer{num}.txt")
    
    with open(filename, "w") as file:
        file.write(content.strip())