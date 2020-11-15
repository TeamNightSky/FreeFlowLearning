from FreeFlowLearning.API.Database import DatabaseManager

db = DatabaseManager('FreeFlowLearning/API/Database/freeflowlearning.db')

db.add_template('testing', id='NUMBER')

print(db.templates)

db.establish_templates()