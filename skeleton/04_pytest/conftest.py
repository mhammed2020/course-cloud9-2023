# import pytest,os,tempfile

# @pytest.fixture
# def get_repository(tmpdir,scope='session'):
#     path = tmpdir.mkdir('repo')
#     os.system("""
#     cd {d}
#     git init 
#     touch A
#     git config user.email 'you@example.com'
#     git config user.name 'Your Name'
#     git add A
#     git commit -m 'A' A
#     """.format(d=path.strpath)
#     return path.strpath