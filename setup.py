from distutils.core import setup
setup(
  name = 'electronicscalc',         
  packages = ['electronicscalc'],   
  version = '0.5',      
  license='MIT',        
  description = 'This is the package that houses various functions which can be used to calculate values for problems involving circuit design , value of the components which are needed to construct the circuit and so on', 
  author = ['Vishal Balaji Sivaraman','Vigneshwar K R'],                
  author_email = 'vb.sivaraman_official@yahoo.com',     
  url = 'https://github.com/The-SocialLion/Electronics-calc',   
  download_url = 'https://github.com/The-SocialLion/Electronics-calc/archive/v_05.tar.gz',    
  keywords = ['electronics', 'calculator', 'Electronics-calculations','circuit-desighn','plot'],   
  install_requires=[           
          'numpy',
          'pandas',
          'Matplotlib',
          'SciPy'
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
