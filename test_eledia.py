from  eledia import eledia_text
import os
import tempfile
import pytest



    
    
@pytest.fixture
def setup_test_directory():
    with tempfile.TemporaryDirectory() as verzeivhnis_ebene_1:
        # Create a nested directory structure as described in the Exercise sheet
        # Create .eledia files with test content
        #############################Ebene-1##############################################
        file_1_level_1 = os.path.join(verzeivhnis_ebene_1, 'a.eledia')
        file_2_level_1 = os.path.join(verzeivhnis_ebene_1, 'x.txt')
        with open(file_1_level_1, 'w') as f:
            f.write('1:content1\n2:content2\n')
        
        with open(file_2_level_1, 'w') as f:
            # Write some content to the file
            f.write("Hello, this is a test file.\n")
        #############################Ebene-2##############################################
        verzeivhnis_ebene_2_1 = os.path.join(verzeivhnis_ebene_1, 'subdir2.1')
        verzeivhnis_ebene_2_2 = os.path.join(verzeivhnis_ebene_1, 'subdir2.2')
        os.makedirs(verzeivhnis_ebene_2_1)
        os.makedirs(verzeivhnis_ebene_2_2)
        file_1_level_2 = os.path.join(verzeivhnis_ebene_2_1, 'c.eledia')
        file_2_level_2 = os.path.join(verzeivhnis_ebene_2_1, 'm.eledia')
        file_3_level_2 = os.path.join(verzeivhnis_ebene_2_2, 'f.eledia')
        file_4_level_2 = os.path.join(verzeivhnis_ebene_2_2, 'y.txt')
        
        with open(file_1_level_2, 'w') as f:
            f.write('1:content3\n3:content4\n')
            
        with open(file_2_level_2, 'w') as f:
            f.write('1:content5\n4:content6\n')
            
        with open(file_3_level_2, 'w') as f:
            f.write('1:content7\n5:content8\n')
            
        with open(file_4_level_2, 'w') as f:
            f.write("Hello, this is a test file.\n") 
            
        #############################Ebene-3##############################################
        verzeivhnis_ebene_3 = os.path.join(verzeivhnis_ebene_2_2, 'subdir3')
        os.makedirs(verzeivhnis_ebene_3)
        file_1_level_3 = os.path.join(verzeivhnis_ebene_3, 'a.txt')
        file_2_level_3 = os.path.join(verzeivhnis_ebene_3, 'z.txt')
        
        with open(file_1_level_3, 'w') as f:
            f.write("Hello, this is a test file.\n")
            
            
        with open(file_2_level_3, 'w') as f:
            f.write("Hello, this is a test file.\n")
            
        #############################Ebene-4##############################################
        verzeivhnis_ebene_4 = os.path.join(verzeivhnis_ebene_3, 'subdir4')
        os.makedirs(verzeivhnis_ebene_4)
        
        file_4_level_4 = os.path.join(verzeivhnis_ebene_4, 'b.eledia')
                
        with open(file_4_level_4, 'w') as f:
            f.write('1:content9\n4:content10\n')

        yield verzeivhnis_ebene_1
'''   
this test check if content in the resulted string are sorted properly
ex.
In level 2, there are two .eledia files (c.eledia and m.eledia) under one directory, 
and another f.eledia file under a different directory within the same level. 
All three files contain the ID '1'. The content of the files in the resulted string
should be sorted alphabetically according to the filenames.
level:1[content1]  level:2[content 3  content 7  content 5] level:3[content9]
        a.eledia            c.eledia   f.eledia   m.eledia          b.eledia
''' 
        
def test_eledia_text_content_sequence_in_resulted_string_level_2(setup_test_directory):
    dir = setup_test_directory
    result = eledia_text(1, dir)
    
    # Verify that the result is as expected
    expected_result = 'content1 content3 content7 content5 content9'
    assert result == expected_result
    
def test_eledia_text_resulted_string_with_two_words(setup_test_directory):
    dir = setup_test_directory
    result = eledia_text(4, dir)
    
    # Verify that the result is as expected
    expected_result = 'content6 content10'
    assert result == expected_result
    
def test_eledia_text_none_existing_id(setup_test_directory):
    dir = setup_test_directory
    result = eledia_text(8, dir)
    
    # Verify that the result is as expected
    expected_result = ''
    assert result == expected_result


    
if __name__ == "__main__":
    pytest.main()   