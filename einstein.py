def main():
    m = int(input("m: "))  # ✅ 僅提示 "m: "
    c = 300_000_000
    E = m * c * c
    print(E)

if __name__ == "__main__":
    main()
