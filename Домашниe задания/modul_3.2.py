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
                                print('Письмо успешно отправлено с адреса <sender> на адрес <recipient>')
                                break
                            else:
                                print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
                                break
                    if net == 'ten.':
                        if sender is recipient:
                            print('Нельзя отправить письмо самому себе!3')
                            break
                        elif sender != recipient:
                            if com1 == 'moc.' or net1 == 'ten.' or ru1 == 'ur.':
                                print('Письмо успешно отправлено с адреса <sender> на адрес <recipient>')
                                break
                            else:
                                print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
                                break

                    if com == 'moc.':
                        if sender is recipient:
                            print('Нельзя отправить письмо самому себе!')
                            break
                        elif sender != recipient:
                            if com1 == 'moc.' or ru1 == 'ur.' or net1 == 'ten.':
                                print('Письмо успешно отправлено с адреса <sender> на адрес <recipient>')
                                break
                            else:
                                print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
                                break
                    else:
                        print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
                        break
                else:
                    print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
                    break
            break
        else:
            print('Невозможно отправить письмо с адреса <sender> на адрес <recipient>')
            break


send_email('vbn', "university.help@gmail.net", "university.helpg@mail.ru" )

