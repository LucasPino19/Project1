def es_letra(car):
    return "a"<=car.lower()<="z"

def es_vocal(car):
    return car.lower() in "aeiouáéíóúü"

def es_consonante(car):
    return car.lower() in "qwrtypsdfghjklñzxcvbnm"
def test():
    m=open("entrada.txt")
    texto=m.read()
    m.close()
    cl=cp=0
    r1=r3=r4=0
    r2 =None
    digito_impar=False
    mayuscula=True
    paso_m=paso_a=True
    inicia_vocal=paso_b=False
    cc=cv=cont=acu=0
    paso_d = d_vocal = False
    dd_vocal =0
    for car in texto:
        if car in " .":
            if cl>0:
                cp+=1
            # punto 1
                if digito_impar and not mayuscula:
                    r1+=1

            # punto 2
                if inicia_vocal and paso_b:
                    if r2 is None or cl>r2:
                        r2=cl
            #punto 3
                if cc > cv and paso_m and paso_a:
                    cont+=1
                    acu+=cl
                    r3=acu//cont
            # punto 4
                if dd_vocal>= 2:
                    r4+=1


            cl=0
            #1
            digito_impar = False
            mayuscula = True

            # 2
            inicia_vocal = paso_b = False
            # 3
            paso_m = paso_a = True
            # 4
            paso_d=d_vocal=False
            dd_vocal =0



        else:
            cl+=1

            # punto 1
            if cl == 1 and car in "13579":
                digito_impar = True

            if es_letra(car):
                mayuscula = True
            else:
                mayuscula=False


            # punto 2
            if cl == 1 and es_vocal(car):
                inicia_vocal = True
            if car in "bB":
                paso_b = True


            # punto 3
            if es_consonante(car):
                cc+=1
            if es_vocal(car):
                cv+=1
            if car in "mM":
                paso_m=False
            if car in "aáAÁ":
                paso_a=False
            # punto 4
            if car in "dD":
                paso_d=True
            else:
                if paso_d and es_vocal(car):
                    dd_vocal+=1
                paso_d=False



    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    test()