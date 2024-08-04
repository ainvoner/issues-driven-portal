import yaml
import sys

def validate_issue(issue_content):
    required_keys = ['apiVersion', 'kind', 'metadata', 'labels', 'repo']
    metadata_keys = ['name']
    labels_keys = ['app']
    repo_keys = ['name', 'owner']

    if not all(key in issue_content for key in required_keys):
        print('Missing top-level keys')
        return False

    if not all(key in issue_content['metadata'] for key in metadata_keys):
        print('Missing metadata keys')
        return False

    if not all(key in issue_content['labels'] for key in labels_keys):
        print('Missing labels keys')
        return False

    if not all(key in issue_content['repo'] for key in repo_keys):
        print('Missing repo keys')
        return False

    return True

if __name__ == "__main__":
    issue_body = sys.argv[1]
    try:
        issue_content = yaml.safe_load(issue_body)
        if not validate_issue(issue_content):
            sys.exit(1)
        else:
            return issue_content['metadata']['name']
    except Exception as e:
        print(f'Error parsing issue content: {e}')
        sys.exit(1)