# +-------+-----+
# | Name  | Age |
# +=======+=====+
# | Alice | 24  |
# +-------+-----+
# | Bob   | 19  |
# +-------+-----+
import csv 


class Table:

    def __init__(self,filepath):
        self.column_title = []
        self.rows = []
        with open(filepath,'r',encoding="utf8") as file:
            csvreader = csv.reader(file)
            self.column_title = next(csvreader)
            self.column_title.insert(0,'# ')

            for row in csvreader:
                self.rows.append(row)
                
    def list_table(self, config):
        start = config['start']
        end = config['end']
        limit = config['limit']

        if int(start) == -1:
            start = len(self.rows) - 1
        if int(end) == -1:
            end = len(self.rows)
        if int(limit) == -1:
            limit = len(self.rows)

        if type(start) != int or type(end) != int :
            raise TypeError(f"type of start and end should be an integer but given start:{type(start)}, end:{type(end)}")
        elif start > len(self.rows) or end > len(self.rows) :
            raise IndexError(f"rows are not available. Total rows : {len(self.rows)} and you are asking for range start:{type(start)}, end:{type(end)}")
        elif end < start :
            raise IndexError(f"end should be greater than or equals to start but given start:{type(start)}, end:{type(end)}")

        index = self.column_title.index(config['search']['column_name'])-1
        value = (config['search']['term']).strip().lower()
        rows = list(filter(lambda x: value in x[index].strip().lower(), self.rows[start:end]))
        rows = rows[:limit]

        table = '+' 

        for title in self.column_title:
            table += ('-')*(len(title)+2)+"+"

        table += ('\n|  '+' | '.join(map(lambda x:x.lower().strip(),self.column_title)) +' |\n+')

        for title in self.column_title:
            table += ('=')*(len(title)+2)+"+"

        row_number = 0
        for row in rows:
            row_number += 1
            table += '\n| '+ str(row_number)+'  |'
            column_index = 1

            for data in row :
                title_length = len(self.column_title[column_index])+1
                data_length = len(data)
                extra_length = title_length - data_length
                table += f" {data[:title_length]}{extra_length*' '}|"
                column_index += 1
            
            table += '\n+'

            for title in self.column_title:
                table += ('-')*(len(title)+2)+"+"
             
        print(table)     

config = {
    "start":50,
    "end":500,
    "limit":10,
    "search": {
        "column_name":'location',
        "term":'United States'
    }    
}
zb = Table("data.csv")
zb.list_table(config)