def reverse(st):
    # Your Code Here
    list1 = st.split()
    list1.reverse()
    st = ' '.join(list1)
    return st