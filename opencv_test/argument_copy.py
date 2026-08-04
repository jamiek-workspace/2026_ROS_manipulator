def argu_a(a):
    a[0] += 1

def main():
    a = [5]
    argu_a(a) # 리스트로 넘기거나 컨테이너로 넘기면 객체의 ID 복사
    print(a)

main()