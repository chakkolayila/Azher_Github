import streamlit as st

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------------
# Initialize Session State
# ----------------------------------
if "students" not in st.session_state:
    st.session_state.students = []

# ----------------------------------
# Grade Function
# ----------------------------------
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# ----------------------------------
# Title
# ----------------------------------
st.title("🎓 Student Grade Manager")
st.write("Add students, calculate grades, and view class statistics.")

# ----------------------------------
# Add Student Form
# ----------------------------------
with st.form("student_form"):

    name = st.text_input("Student Name")

    mark = st.number_input(
        "Student Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:

        if name.strip() == "":
            st.error("Please enter a student name.")

        else:
            st.session_state.students.append(
                {
                    "Name": name,
                    "Mark": mark,
                    "Grade": calculate_grade(mark)
                }
            )

            st.success(f"{name} added successfully!")

# ----------------------------------
# Display Student Table
# ----------------------------------
st.subheader("📋 Student Records")

if len(st.session_state.students) > 0:

    st.table(st.session_state.students)

    # Statistics
    marks = [student["Mark"] for student in st.session_state.students]

    average_mark = sum(marks) / len(marks)
    highest_mark = max(marks)
    lowest_mark = min(marks)

    st.subheader("📊 Class Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Average Mark", f"{average_mark:.2f}")

    with col2:
        st.metric("Highest Mark", highest_mark)

    with col3:
        st.metric("Lowest Mark", lowest_mark)

else:
    st.info("No students have been added yet.")

# ----------------------------------
# Clear All Data
# ----------------------------------
if st.button("🗑️ Clear All Students"):
    st.session_state.students = []
    st.rerun()