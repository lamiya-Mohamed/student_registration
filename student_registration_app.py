import streamlit as st

st.title("🎓 نظام تسجيل الطلاب")

# إنشاء قائمة الطلاب في الذاكرة
if "students_list" not in st.session_state:
    st.session_state.students_list = []

# إدخال الاسم
name_student = st.text_input("إدخال اسم الطالب:")

# زر التسجيل
if st.button("تسجيل الطالب"):
    if name_student:
        st.session_state.students_list.append(name_student)
        st.success(f"✅ تم تسجيل {name_student} بنجاح!")
    else:
        st.warning("⚠️ من فضلك أدخل اسم الطالب أولاً.")

# عرض قائمة الطلاب
if st.session_state.students_list:
    st.subheader("📋 قائمة الطلاب المسجلين:")
    for student in st.session_state.students_list:
        st.write(f"- {student}")

    # حساب العدد
    registered_students = len(st.session_state.students_list)
    st.info(f"👥 إجمالي عدد الطلاب المسجلين: {registered_students}")
else:
    st.write("لم يتم تسجيل أي طلاب بعد.")

# زر لإعادة التشغيل
if st.button("🔄 إعادة تعيين القائمة"):
    st.session_state.students_list = []
    st.success("✅ تم مسح قائمة الطلاب.")
