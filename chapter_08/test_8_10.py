kebis = ['Hi','man!','what can I say!','Manba out']
sent_messages = []

def show_message(messages):
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)

def send_messages(old_list,new_list):
    print(f'\n原列表当前内容为:')
    print(old_list)
    print(f'\n新列表当前内容为:')
    print(new_list)

show_message(kebis[:])
send_messages(kebis,sent_messages)