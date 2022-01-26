import unittest
import ipv4 as prf
# https://github.com/yroosel/PythonExperiments/blob/5e91726faf3ff83aa80e2b04a34299dc2aa7c882/unittest/ipv4.py

class test_ip_subnet_prefixes(unittest.TestCase):

   def test_get_net_prefix(self):
       self.assertEqual(prf.get_net_prefix('255.255.255.252'), '/30')   
       #self.assertTrue()
       #self.assertFalse()
       #with self.assertRaises(TypeError):
      
   def test_get_netmask(self):
       self.assertEqual(prf.get_netmask('/30'), '255.255.255.252')   

   def test_get_number_ip_addresses(self):
       self.assertEqual(prf.get_number_ip_addresses('/30'), 4)   

   def test_get_number_ip_hosts(self):
       self.assertEqual(prf.get_number_ip_hosts('/30'), 2)

   def test_get_network_bits(self):
       self.assertEqual(prf.get_network_bits('255.255.255.252') , '1111 1111 1111 1111 1111 1111 1111 1100')

if __name__ == '__main__':
   unittest.main()

