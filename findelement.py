import time
listContainer = [
                i
                for i in range(1000)
                ]
setContainer = {
                i
                for i in range(1000)
                }

def checkContainer(number, container):
    if number in container:
        print(number, "is in container")
        return True
    else:
        print(number, "is not in container")
        return False

def timeCounter(func, number, list):
    start = time.perf_counter()
    func(number,listContainer)
    end = time.perf_counter()
    print(start-end)


timeCounter(checkContainer, 700, listContainer)
timeCounter(checkContainer, 700, setContainer)