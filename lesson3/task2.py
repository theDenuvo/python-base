def info(name, sname, bday, city, email, phone):
    """

    :param name: string
    :param sname: string
    :param bday: string
    :param city: string
    :param email: string
    :param phone: sting
    :return:
    """
    print(f"{name} {sname}, <{email}>, ({phone}), {city}, дата рождения: {bday}, ")


info(name=input(),
    sname=input(),
    bday= input(),
     city=input(),
    email=input(),
    phone=input(),
    )