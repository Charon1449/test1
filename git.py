import json
from github import Github


workflow_files = ('pylint.yml' ,'pytest.yml')
file_name = 'names.json'
user_github_pseudo = "Charon1449"
repo_name = 'Skill-test-tool'
access_token = "3dba8d03af4b7ad48e776b6336dacb91ee238b27"






def create_workflows(workflow_files ,repo):
    for workflow in workflow_files:
        workflow_path = '.github/workflows/' + workflow
        repo.create_file(workflow_path,"adding workflow",open(workflow).read())


def add_collaborators(file_name, repo):
    json_data = json.loads(open(file_name).read())
    for condidat in json_data:
        repo.add_to_collaborators(condidat['Github'],"push")

def create_branchs(file_name, repo):
    json_data = json.loads(open(file_name).read())
    source_branch = 'master'
    for condidat in json_data:
       target_branch = "branch_of_" + condidat['Name'].replace(' ','_')
       sb = repo.get_branch(source_branch)
       repo.create_git_ref(ref='refs/heads/'+ target_branch ,sha=sb.commit.sha )




g = Github(access_token)
user = g.get_user()
repo = g.get_repo(user_github_pseudo + '/' + repo_name )



print("Repo name : " + repo.name)
print("User : " + user.name)
print(list(repo.get_branches()))


repo.add_to_collaborators("eugenes1449" ,"push")






'''
print('---------------------------')
print('---adding collaborators----')
#add_collaborators(file_name, repo)
print('---------------------------')

print('---------------------------')
print('---Creating branches-------')
create_branchs(file_name, repo)
print('---------------------------')

print('---------------------------')
print('---Adding workflows--------')
create_workflows(workflow_files ,repo)
print('---------------------------')


'''














