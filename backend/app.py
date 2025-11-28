courses = [
 [" الذكاء الاصطناعي", 100],
    ["الشبكات والأمن السيبراني", 100],
    ["تحليل الهجمات السيبرانية", 100],
    ["بايثون ", 100],
    ["تصميم واجهات الويب HTML و CSS", 500]
]
while True:
    print("\nاختر رقم الدورة للتسجيل:")

    for number, course_item in enumerate(courses, start=1):
        print(f"{number}. {course_item[0]} - السعر: {course_item[1]} ريال")

    user_input = input("اكتب الرقم (أو اكتب 'خروج' لإنهاء البرنامج): ")

    if user_input.lower() == "خروج":
        print("تم إنهاء البرنامج. شكرًا لك!")
        break
    if user_input.isdigit():
        selected = int(user_input)
        if 1 <= selected <= len(courses):
            course_name, course_price = courses[selected - 1]
            total_price = course_price * 1.15  # الضريبة 15%
            print(f"السعر شامل الضريبة للدورة '{course_name}' هو: {total_price:.2f} ريال")
        else:
            print(f"الرقم غير صحيح! اختر رقمًا بين 1 و {len(courses)}")
    else:
        print("يرجى إدخال رقم صالح")