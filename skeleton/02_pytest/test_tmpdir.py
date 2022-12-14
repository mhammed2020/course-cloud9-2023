import os 
def test_create_file(tmpdir):
    
    path = tmpdir.mkdir('subdir').join('file.txt')
    path.write('content')
    print(path.strpath)
    assert 0
    
    # assert os.path.isfile(path.strpath)