import problem8

def test_script() :
    st = 'hello'
    st2='HELLO'
    assert problem8.make_lower(st2)==st.lower()
    assert problem8.make_upper(st)==st.upper()
    assert problem8.make_capital(st)==st.capitalize()