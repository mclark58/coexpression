# Test script for genome_util package - it should be launched from
# the root of the genome_util module, ideally just with 'make test', as
# it looks for a hardcoded relative path to find the 'test.cfg' file
import unittest
import json
import ConfigParser

from pprint import pprint

from subprocess import call

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint


from biokbase.CoExpression.authclient import KBaseAuth as _KBaseAuth

from biokbase.auth import Token

# Before all the tests, read the config file and get a user token and
# save it to a file used by the main service script
class TestCoExpressionMethodsSetup(unittest.TestCase):
<<<<<<< Updated upstream
  def setUp(self):
    config = ConfigParser.RawConfigParser()
    config.read('ltest/test.cfg')
    user_id = config.get('CoExpressionTest','user')
    password = config.get('CoExpressionTest','password')
    token = Token(user_id=user_id, password=password)
    token_file = open('ltest/script_test/token.txt','w')
    token_file.write(token.token)

# Define all our other test cases here
class TestCoExpressionMethods(TestCoExpressionMethodsSetup): 

 def test_filter_genes(self):
        print("\n\n----------- test filter genes ----------")

        out =call(["run_CoExpression.sh",
        "ltest/script_test/test_filter_genes_input.json",
        "ltest/script_test/test_filter_genes_output.json",
        "ltest/script_test/token.txt"])

        # print error code of Implementation
        print(out);

        with open('ltest/script_test/test_filter_genes_output.json') as o:
                output =json.load(o)
        pprint(output)

 def test_coex_cluster(self):
        print("\n\n----------- test constcoex_net_clust ----------")

        out =call(["run_CoExpression.sh",
        "ltest/script_test/test_coex_clust_input.json",
        "ltest/script_test/test_coex_clust_output.json",
        "ltest/script_test/token.txt"])

        # print error code of Implementation
        print(out);

        with open('ltest/script_test/test_coex_clust_output.json') as o:
                output =json.load(o)
        pprint(output)
=======

    @classmethod
    def setUp(cls):
      token = environ.get('KB_AUTH_TOKEN', None)
      config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
      cls.cfg = {}
      config = ConfigParser()
      config.read(config_file)
      for nameval in config.items('CoExpression'):
            cls.cfg[nameval[0]] = nameval[1]
      authServiceUrl = cls.cfg.get('auth-service-url',
                                     "https://kbase.us/services/authorization/Sessions/Login")
      auth_client = _KBaseAuth(authServiceUrl)
      user_id = auth_client.get_user(token)
      print('>>>>>>>>>authServiceUrl: '+authServiceUrl)
      print('>>>>>>>>>user_id: ' + user_id)

      #config = ConfigParser.RawConfigParser()
      #config.read('ltest/test.cfg')
      #user_id = config.get('CoExpressionTest','user')
      #password = config.get('CoExpressionTest','password')
      #token = Token(user_id=user_id, password=password)
      token_file = open('ltest/script_test/token.txt','w')
      token_file.write(token)




  # Define all our other test cases here
class TestCoExpressionMethods(TestCoExpressionMethodsSetup):

   def test_diff_p_distribution(self):
          print("\n\n----------- test diff_p_distribution  ----------")

          out =call(["run_CoExpression.sh",
          "ltest/script_test/test_diff_p_distribution_input.json",
          "ltest/script_test/test_diff_p_distribution_output.json",
          "ltest/script_test/token.txt"])

          # print error code of Implementation
          print(out);

          with open('ltest/script_test/test_diff_p_distribution_output.json') as o:
                  output =json.load(o)
          pprint(output)

   def test_view_heatmap(self):
          print("\n\n----------- test view_heatmap  ----------")

          out =call(["run_CoExpression.sh",
          "ltest/script_test/test_view_heatmap_input.json",
          "ltest/script_test/test_view_heatmap_output.json",
          "ltest/script_test/token.txt"])

          # print error code of Implementation
          print(out);

          with open('ltest/script_test/test_view_heatmap_output.json') as o:
                  output =json.load(o)
          pprint(output)

   def test_filter_genes(self):
          print("\n\n----------- test filter genes ----------")

          out =call(["run_CoExpression.sh",
          "ltest/script_test/test_filter_genes_input.json",
          "ltest/script_test/test_filter_genes_output.json",
          "ltest/script_test/token.txt"])

          # print error code of Implementation
          print(out);

          with open('ltest/script_test/test_filter_genes_output.json') as o:
                  output =json.load(o)
          pprint(output)

   def test_coex_cluster(self):
          print("\n\n----------- test constcoex_net_clust ----------")

          out =call(["run_CoExpression.sh",
          "ltest/script_test/test_coex_clust_input.json",
          "ltest/script_test/test_coex_clust_output.json",
          "ltest/script_test/token.txt"])

          # print error code of Implementation
          print(out);

          with open('ltest/script_test/test_coex_clust_output.json') as o:
                  output =json.load(o)
          pprint(output)

>>>>>>> Stashed changes


#start the tests if run as a script
if __name__ == '__main__':
    unittest.main()
