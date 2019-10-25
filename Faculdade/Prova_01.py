#Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Fazer um programa (em linguagem Python) que 
#solicite a massa inicial (em gramas) e que calcule o tempo necessário para que essa massa se torne menor que 0,5 grama. 
#Ao término, o programa deve exibir a massa inicial, a massa final e o tempo calculado em horas, minutos e segundos

m_ini = float(input('Digite o valor da massa (g): '))
m = m_ini
cont = 0
while m >= 0.5:
    m = m / 2
    cont += 1
segundos = cont * 50
horas = segundos // 3600
resto_segundos = segundos % 3600
minutos = resto_segundos // 60
resto_minutos = resto_segundos % 60
print ('-'*40)
print ('Massa inicial:', m_ini)
print ('Massa final:', m)
print ('Tempo em segundos: ',segundos)
print ('Tempo:',horas,'H',minutos,'M',resto_minutos,'S')
print ('-'*40)