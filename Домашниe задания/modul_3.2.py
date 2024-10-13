def send_email( message, recipient,*, sender = "university.help@gmail.com"):
    for _ in sender:
        if '@' in sender:
            for j in recipient:
                if '@' in recipient:
                    if sender != recipient:
                        sen = sender.endswith(('.ru', '.com', '.net'))
                        if sen is True:
                            rec = recipient.endswith(('.ru', '.com', '.net'))
                            if rec is True:
                                if sender == "university.help@gmail.com":
                                    print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                                    break
                                else:
                                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
                                    break


                            else:
                                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без расширения <.com>, <ru>, <net> в <recipient>')
                                break
                        else:
                            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без расширения <.com>, <.ru>, <.net> в <sender>')
                            break
                    elif sender is recipient:
                        print('Нельзя отправить письмо самому себе!')
                        break
                else:
                    print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без <@> в <recipient>')
                    break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient} без <@> в <sender>')
            break
        break

send_email('vbn', "university.helpg@mil.net", sender = "uni.help@gmail.com")

