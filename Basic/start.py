print("Hello, Python")

# 변수
message = "Hello, python"
print(message)

# print(mesage)
# 에러
print("traceback")
print("#1 첫 째줄 에러 위치")
print("#2 에러를 일으킨 내용")
print("#3 에러 발생한 이유")

# String 문자열
name = 'hermione granger'
gender = "female"
print(name.title())
name = name.upper()
print(name)
name = name.lower() #사용자가 대소문자를 햇갈리는 경우가 많으므로 일단 lower() 후 알맞은 형태로 변환해서 사용
print(name)
first_name = "hermione"
second_name= "granger"
full_name = f"{first_name} {second_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

# 분리
hello = f"Hello, {full_name.title()}!"
print(hello)

# 탭 추가와 줄바꿈

print("\t 공포 괴담 \n아무도 알지 못한 충격실화!\n절찬 상영중!")
