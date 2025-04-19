# Python Genuis Features

# # Context Manager
# class ContextManager:
#     def __init__(self, file, mode):
#         self.file = open(file, mode)

#     def __enter__(self):
#         return self.file
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()

# with ContextManager('test.txt', 'w') as f:
#     f.write('A Temp File')

# Metaclasses
