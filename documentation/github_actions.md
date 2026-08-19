# GitHub Actions CI/CD Results

This lab demonstrated Continuous Integration using GitHub Actions.

The workflow automatically validated network configuration files
whenever changes were pushed to GitHub.

The workflow successfully:

- Checked repository changes
- Installed Python dependencies
- X Validated JSON files
- Validated YAML files
- Displayed workflow logs

## Validation Results

JSON files:

Router, laptop and server configuration files were successfully and
failure validated.

YAML files:

Switch configuration files were successfully validated.

## Error Testing

A JSON formatting error was introduced.

GitHub Actions detected the error and failed the workflow.

After correcting the JSON file, the workflow completed successfully.

## Comparison

Previously configuration files were checked manually.

Using GitHub Actions, validation is performed automatically whenever changes are pushed.

This improved reliability and reduces configuration errors.