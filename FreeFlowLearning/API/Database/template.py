from FreeFlowLearning.API.Utils import string_quotes


class QueryTemplate:
    def __init__(self, *args, **kwargs):
        self.dict_template = kwargs
        self.name = args[0]
        self.cast_queue = []
    
    def create_query(self):
        str_template = f"CREATE TABLE IF NOT EXISTS {self.name} (\n"

        for index in self.dict_template.keys():
            str_template += f"{index} {self.dict_template[index]}, \n"

        str_template += ");"

        return str_template

    def cast(self, *args):
        self.cast_queue.append(f"  ({', '.join([string_quotes(val) for val in args])})")

    def commit_repr(self, *args, **kwargs):
        str_template = f"""
        INSERT INTO
        {self.name} ({', '.join(self.dict_template.keys())})
        VALUES
          """ + ',\n  '.join(cast_queue) + ';'
        return str_template

