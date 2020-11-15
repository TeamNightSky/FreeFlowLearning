from FreeFlowLearning.API.Utils import string_quotes


class QueryTemplate:
    def __init__(self, *args, **kwargs):
        self.dict_template = kwargs
        self.name = args[0]
        self.commit_queue = []
    
    def create_query(self) -> str:
        """
        .create_query returns a string to 
        be used to create a SQL table for 
        this template
        """
        str_template = f"CREATE TABLE IF NOT EXISTS {self.name} (\n"

        values = []
        for index in self.dict_template.keys():
            values.append(f"  {index} {self.dict_template[index]}")

        return str_template + ',\n'.join(values) + "\n);"

    def cast(self, *args):
        self.commit_queue.append(f"  ({', '.join([string_quotes(val) for val in args])})")

    def commit_repr(self, *args, **kwargs) -> str:
        str_template = f"""
        INSERT INTO
        {self.name} ({', '.join(self.dict_template.keys())})
        VALUES
          """ + ',\n  '.join(commit_queue) + ';'
        return str_template
