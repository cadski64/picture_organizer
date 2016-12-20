
class FileDuplicates(list):

    FileDuplicate = None

    def __getitem__(self, item):
        

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.append((False, from_number, time_arrived, text_of_SMS))    #append tuple to self

    def message_count(self):
        return len(self)