# passwd-parser

# Description


## Name 
passwd-parser - A toy utility to parse /etc/passwd in unix machines and provide corresponding uid, full_name and groups from /etc/group


## Usage
Write in Terminal as follows:
``` shell
python passwd-parser.py [passwd_path] [group_path]
```

## Arguments
Describes all Arguments to Passwd-Parser
```
passwd_path	  path to passwd file       # default /etc/passwd
group_path	  path to group file        # default /etc/group
```

## Examples
Write in Terminal as follows:
``` shell
python passwd-parser.py
python passwd-parser.py /etc/passwd /etc/group
```

## Sample Object
``` shell
{
  "ubuntu": {
          "uid": "1000",
           "full_name": "Ubuntu", 
           "groups": [
                      "adm",
                      "cdrom",

                      "docker",
                      "netdev",
                      "plugdev",
                      "floppy",
                      "audio",
                      "sudo",
                      "video"] 
            },
            
     "man": {
          "uid": "6",
          "full_name": "man",
          "groups": []
}
```

## Author
Written by Saumil Shah. <a href="https://github.com/hellosaumil "> https://github.com/hellosaumil </a>
<br> More details about this project can be found at : <a href="https://github.com/hellosaumil/passwd-parser"> https://github.com/hellosaumil/passwd-parser </a>

## Reporintg Bugs
Report bugs to <a href="https://github.com/hellosaumil/passwd-parser/issues"> https://github.com/hellosaumil/passwd-parser/issues </a>
