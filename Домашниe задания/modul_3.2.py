print('Вариант 1')
def send_email(message, recipient, sender="university.help@gmail.com"):
    for _ in sender:
        if '@' in sender:
            for j in recipient:
                if '@' in recipient:
                    if sender != recipient:
                        sen = sender.endswith(('.ru', '.com', '.net'))
                        if sen is True:
                            rec = recipient.endswith(('.ru', '.com', '.net'))
                            if rec is True:
                                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                                break
                            else:
                                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без расширения <.com>, <ru>, <net> в <recipient>')
                                break
                        else:
                            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без расширения <.com>, <.ru>, <.net> в <sender>')
                            break
                    elif sender == recipient:
                        print('Нельзя отправить письмо самому себе!')
                        break
                else:
                    print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без <@> в <recipient>')
                    break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без <@> в <sender>')
            break
        break

send_email('vbn', "university.helpg@mil.net", "university.helpg@mail.net")





print('Вариант 2')

def send_email(message, recipient, sender="university.help@gmail.com"):
    for _ in sender:
        if '@' in sender:
            for j in recipient:
                if '@' in recipient:
                    send = sender[::-1]  # начало после @
                    com = send[0:4]
                    net = send[0:4]
                    ru = send[0:3]
                    recip = recipient[::-1]
                    com1 = recip[0:4]
                    net1 = recip[0:4]
                    ru1 = recip[0:3]

                    if ru == 'ur.':
                        if sender is recipient:
                            print('Нельзя отправить письмо самому себе!')
                            break
                        elif sender != recipient:

                            if com1 == 'moc.' or net1 == 'ten.' or ru1 == 'ur.':
                                print(f'Письмо успешно отправлено с адреса {sender}  на адрес {recipient}')
                                break
                            else:
                                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без расширения <.com>, <ru>, <net> в <recipient>')
                                break
                    if net == 'ten.':
                        if sender is recipient:
                            print('Нельзя отправить письмо самому себе!')
                            break
                        elif sender != recipient:
                            if com1 == 'moc.' or net1 == 'ten.' or ru1 == 'ur.':
                                print(f'Письмо успешно отправлено с адреса {sender}  на адрес {recipient}')
                                break
                            else:
                                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без расширения <.com>, <ru>, <net> в <recipient>')
                                break

                    if com == 'moc.':
                        if sender is recipient:
                            print('Нельзя отправить письмо самому себе!')
                            break
                        elif sender != recipient:
                            if com1 == 'moc.' or ru1 == 'ur.' or net1 == 'ten.':
                                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                                break
                            else:
                                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient} без расширения <.com>, <ru>, <net> в <recipient>")
                                break
                    else:
                        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без расширения <.com>, <.ru>, <.net> в <sender>')
                        break
                else:
                    print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без <@> в <recipient>')
                    break
            break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без <@> в <sender>')
            break


send_email('vbn', "university.helpg@mail.net", "university.helpg@mail.ru" )

