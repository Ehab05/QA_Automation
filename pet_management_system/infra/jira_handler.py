import os

from jira import JIRA

from API_test_project_part_b.infra.config_provider import ConfigProvider


class JiraHandler:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(base_dir, '../pet_store_management.json')
        secret_file_path = os.path.join(base_dir, '../private.json')
        self._config = ConfigProvider().load_from_file(config_file_path)
        self._secret = ConfigProvider().load_from_file(secret_file_path)
        self._jira_url = self._config["jira_url"]
        self._auth_jira = JIRA(
            basic_auth=(self._config["jira_email"], self._secret["api_token"]),
            options={'server': self._jira_url}
        )

    def create_issue(self, project_key, summary, description, issue_type="Bug"):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }

        return self._auth_jira.create_issue(fields=issue_dict)

    def issue_description(self, error, test_case):
        # generating issue description for the jira report
        return f"{error} in Test Case: {test_case}"
