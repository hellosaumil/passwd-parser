#!/usr/bin/env python
# coding: utf-8
# Brain Corp Challenges for Summer Intern 2019

'''
@author: Saumil Shah
'''

import os
import sys
import json

class PasswdParser:
    """PasswdParser
    A class for Parser Passwd Files in Unix
    """

    def __init__(self, sys_argv):
        """"AudioFrames(filename, adv_ms, len_ms)
        Create a stream of audio frames where each is in len_ms milliseconds long
        and frames are advanced by adv_ms.
        """

        self.passwd_path, self.group_path = '/etc/passwd', '/etc/group'

        total_args = len(sys_argv)

        if total_args == 1:
            pass

        elif (total_args > 2 and total_args < 4):
            self.passwd_path, self.group_path = sys.argv[1:]

        else:
                self.showHelp()
                raise Exception("\n\t**** Invalid Arguments - See Help Above!")

        if self.filesCheck(self.passwd_path, self.group_path):
            self.beginParsing()


    def filesCheck(self, passwd_path, group_path):

        passwd_path_flag = os.path.isfile(passwd_path)
        group_path_flag = os.path.isfile(group_path)

        if not passwd_path_flag:
            raise Exception("\n\t**** Passwd File NOT Found! at {}\n".format(passwd_path))

        if not group_path_flag:
            raise Exception("\n\t**** Group File NOT Found! at {}\n".format(group_path))

        return True


    def readFileLines(self, file_path):
        fileLines = []

        with open(file_path, 'r') as infile:
            try:
                fileLines = infile.readlines()

            except Exception as e:
                raise Exception("\n\t**** Exiting Program With Exception in Reading {} : {}".format(file_path, e))

        return fileLines


    def beginParsing(self):

        group_file_data = self.readFileLines(self.group_path)
        passwd_file_data = self.readFileLines(self.passwd_path)

        users_to_primary_group_map, group_dict = self.parseGroupFile(group_file_data)
        users_object = self.parsePasswdFile(passwd_file_data, users_to_primary_group_map, group_dict)

        print (json.dumps(users_object, indent=4, sort_keys=True))


    def parseGroupFile(self, group_file_data):

        if len(group_file_data) == 0:
            raise Exception("\n\t**** Malformed Groups File!\n")

        else:
            grp_extras = 0
            grp_dict = {}
            users_grp_map = {}

            for g in group_file_data:
                g_val = g.split(':')

                if len(g_val) == 4:
                    users = g_val[3].strip()
                    grp_dict[g_val[2]] = {"gname" : g_val[0], 'pwd': g_val[1], 'users': users}

                    for usr in users.split(','):
                        if usr:
                            try:
                                users_grp_map[usr].append(g_val[0])
                            except:
                                users_grp_map[usr] = [g_val[0]]
                        else:
                            pass
                else:
                    grp_extras += 1

                return users_grp_map, grp_dict

    def parsePasswdFile(self, passwd_file_data, users_to_primary_group_map, group_dict):

        if len(passwd_file_data) == 0:
            raise Exception("\n\t**** Malformed Passwd File!\n")

        else:
            pwd_extras = 0
            pwd_dict = {}

            for p in passwd_file_data:
                p_val = p.split(':')
                groups_of_a_user = []

                if len(p_val) == 7:

                    try:
                        groups_of_a_user = [group_dict[p_val[3]]['gname']]
                        groups_of_a_user += users_to_primary_group_map.get(p_val[0], None)

                        try:
                            groups_of_a_user.remove(None)
                        except:
                            pass

                    except Exception as e:
                        pass

                    pwd_dict[p_val[0]] = {'uid' : p_val[2], 'full_name': p_val[4], 'groups': list(set(groups_of_a_user))}

                else:
                    pwd_extras += 1

            return pwd_dict

    def showHelp(self):
        print (" *********** \n")
        print (" Usage: ")

        print ("\t1. Please run as follows: \
        \n\t\t'passwd-parser.py' \
         \n\n\t -- OR -- \n\n \
        2. Please provide 2 arguments as follows: \
        \n\t\t'passwd-parser.py [passwd_path] [group_path]' \
        \n\n\t\t\t Where passwd_path = path to passwd file \
        \n\t\t\t       group_path = path to group file")

        print (" *********** \n")

if __name__ == '__main__':

    PasswdParser(sys.argv)
