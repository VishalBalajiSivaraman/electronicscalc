from distutils.core import setup
setup(
  name = 'electronicscalc',         
  packages = ['electronicscalc'],   
  version = '0.3',      
  license='MIT',        
  description = 'this is a package houses various steps templates which can be used to calculate values for problems involving design of circuits , verification of circuits and so on',   # Give a short description about your library
  author = 'Vishal Balaji Sivaraman',                   
  author_email = 'vb.sivaraman_official@yahoo.com',     
  url = 'https://github.com/The-SocialLion/Electronics-calc',   
  download_url = 'https://github.com/The-SocialLion/Electronics-calc/archive/v_03.tar.gz',    
  keywords = ['electronics', 'calculator', 'Electronics-calculations','circuit-desighn','plot'],   
  install_requires=[           
          'numpy',
          'pandas',
          'Matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',    
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
