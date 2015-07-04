# ansible-role-obnam
Ansible role for installing and configuring [obnam](http://obnam.org/) to perform regular
backups.

# Example

To user it, simply put this in your playbook:

```yaml
- role: obnam
  repository: sftp://someuser@backupserver/somebackupfolder
  backup_src: ['/home/someuser/somefolder']
```

# Variables

## repository
The obnam repository to which we should backup.
This is a mandatory variable and can be either a local path or an URL
in the form "sftp://[user@]domain[:port]/path".
For more details on the acceptable formats please see obnam(1).

## keep\_policy (default "7d,4w,12m")
Keep policy for obnam. How many days, weeks, months and years should
be kept as backups. See obnam(1) for accepted formats.

## user\_account (default: root)
User account that will call obnam on the source host.

## ssh\_key
Path to the SSH key to use when connecting to backup repository.
The path is relative to the home directory of {{user\_account}} and if
it's not supplied it uses ssh's default key.

## backup\_src
Directories to backup.
If you have obnam >= 1.9, you can also backup individual files.

## backup\_frequency (default "daily")
Frequency obnam gets called. Acceptable vaules are the same as the
"special\_time" attribute of the "cron" ansible module.
If not provided, obnam will be set up, but no cronjob will be created.

# Limitations

 - Currently supports only one backup job per user.
