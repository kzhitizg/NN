import matplotlib.pyplot as plt

ip = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
op = [-1, 1, 1, 1]

w1 = w2 = wb = 0.1
alpha = .0001
epc = 1
thr=0.002

while True:
    error=0
    for i in range(len(op)):
        x = ip[i]
        yin = w1*x[0] + w2*x[1] + wb*1
        error+=(op[i]-yin)**2
        dl = alpha*(op[i]-yin)
        w1 += x[0]*dl
        w2 += x[1]*dl
        wb += dl
        # print("After epoc {}, error={}, weights- w1={}, w2={}, wb={}".format(epc,error, w1, w2, wb))

    if epc %1000 == 0:
        print("After epoc {}, error={}, weights- w1={}, w2={}, wb={}".format(epc,error, w1, w2, wb))
    epc+=1
    if error<thr:
        break
    if epc >= 10000:
        plt.title("Epoch " + str(epc))
        for j in range(len(ip)):
            if op[j] == 1:
                mk = "+"
            else:
                mk = "_"
            plt.scatter(ip[j][0], ip[j][1], marker=mk)
        plt.plot([-3, 3], [(3*w1 - wb)/w2, (-3*w1 - wb)/w2])
        plt.show()
        break
    

print("Final outputs- w1={}, w2={}, wb={}, error={}".format(w1, w2, wb, error))