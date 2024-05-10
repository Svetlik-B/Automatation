import pytest
from class_string_utils import StringUtils


sut = StringUtils()

@pytest.mark.parametrize("string, result",
                        [("skypro", "Skypro"),
                        ("", ""),
                        (" "," "), 
                        ("test", "Test"), 
                        ("tesT", "Test"),
                        (" test", " test"), 
                        ("123", "123"),
                        ("123 456", "123 456"),
                        ("123 test", "123 test"),
                        ("str str str", "Str str str") 
                        ])
def test_capitalize(string, result):
     assert sut.capitilize(string) == result
    
 
    # assert sut.capitilize("") == ""    
    # assert sut.capitilize(" ") == " "   
    # assert sut.capitilize("test") == "Test"
    # assert sut.capitilize("tesT") == "Test" 
    # assert sut.capitilize(" test") == " test"
    # assert sut.capitilize("123") == "123"
    # assert sut.capitilize("123 456") == "123 456"
    # assert sut.capitilize("123 test") == "123 test"
    # assert sut.capitilize("str str str") == "Str str str"    
    
    
# print(sut.trim("   skypro"))    
def test_trim():
    assert sut.trim("  skypro") == "skypro"    
    assert sut.trim("") == ""    
    assert sut.trim(" ") == ""   
    assert sut.trim("  123") == "123"
    assert sut.trim("без пробела") == "без пробела"
    assert sut.trim("пробел в конце   ") == "пробел в конце   "
    assert sut.trim("   пробел в конце   ") == "пробел в конце   "
    assert sut.trim("пробел в    середине") == "пробел в    середине"
    assert sut.trim("  пробел в    середине") == "пробел в    середине"
    
       
# print(sut.to_list("a,b,c,d"))
def test_to_list():
    assert  sut.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert  sut.to_list(",,,") == ["", "", "", ""]
    assert  sut.to_list("") == []
    assert  sut.to_list("1!2!3", "!") == ["1", "2", "3"]
    assert  sut.to_list("1:23", ":") == ["1", "23"]
    assert  sut.to_list("1:2:3", " ") == ["1:2:3"]
    assert  sut.to_list("1,2,,,3", ",,") == ["1,2",",3"] 
    assert  sut.to_list("1,2,,,,,3", ",,") == ["1,2", "", ",3"] 
    
    
# print(sut.contains("SkyPro", "P"))
def test_contains():
    assert sut.contains("SkyPro", "S") == True
    assert sut.contains("SkyPro", "U") == False
    assert sut.contains("SkyPro", "p") == False
    assert sut.contains("SkyPro", "") == True
    assert sut.contains("SkyPro", "ky") == True
    assert sut.contains("SkyPro", "yk") == False


# print(sut.delete_symbol("SkyPro", "k"))
def test_delete_symbol():
    assert sut.delete_symbol("", "") == ""
    assert sut.delete_symbol(" ", " ") == ""
    assert sut.delete_symbol("?!", "!") == "?"
    assert sut.delete_symbol("Sky Pro", " ") == "SkyPro"
    assert sut.delete_symbol("123", "3") == "12"
    assert sut.delete_symbol("04 апреля 2023", "02") == "04 апреля 23"
    
    
# print(sut.starts_with("SkyPro", "S"))
def test_starts_with():
    assert sut.starts_with("Training", "Training") == True
    assert sut.starts_with("Training", "T") == True
    assert sut.starts_with("Training", "A") == False
    assert sut.starts_with(" ", " ") == True
    assert sut.starts_with("", "") == True
    assert sut.starts_with(" ", "") == True
    assert sut.starts_with("19999", "1") == True
    assert sut.starts_with("19999", "") == True
    assert sut.starts_with(";:!", ";") == True
    assert sut.starts_with(";;", " ") == False
 
    
# print(sut.end_with("SkyPro", "o"))
def test_end_with():
    assert sut.end_with("Hello World", "") == True
    assert sut.end_with("Hello World", "d") == True
    assert sut.end_with("Hello World", "Hello World") == True
    assert sut.end_with("Hello World", "o") == False
    assert sut.end_with("Hello ", " ") == True
    assert sut.end_with(" ", " ") == True
    assert sut.end_with("", "") == True
    assert sut.end_with("9 11", "1") == True
    assert sut.end_with("New,", ",") == True
    
    
# print(sut.is_empty(""))
def test_is_empty():
    assert sut.is_empty("Hello") == False
    assert sut.is_empty(" ") == True
    assert sut.is_empty("") == True
    
    
# print(sut.list_to_string([1,2,3,4]))
def test_list_to_string():
    assert sut.list_to_string(["SkyPro","Homework"]) == "SkyPro, Homework"
    assert sut.list_to_string([1,"m"], " - ") == "1 - m"
    assert sut.list_to_string([""]) == ""
    assert sut.list_to_string([","]) == ","
    assert sut.list_to_string(["00000, 9"]) == "00000, 9"
    assert sut.list_to_string(["0 yeah, 9"]) == "0 yeah, 9"
    assert sut.list_to_string(["0 yeah 9, 9"]) == "0 yeah 9, 9"
    assert sut.list_to_string(["00","0"]) == "00, 0"
    assert sut.list_to_string(["00" "0"], "+") == "000"
    assert sut.list_to_string(["00","0"], "!") == "00!0"
     