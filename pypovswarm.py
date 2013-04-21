'''
Created on 20.04.2013

@author: maweki
'''

import json

fac = 10

if __name__ == '__main__':
    print '#declare tex = \
        texture{ \n pigment{ color rgb<1,1,1>} \n\
        finish {ambient 0.1 \n\
                 diffuse 0.9 \n\
                 phong 1}}\n'
    print '#declare texa = \
        texture{ \n pigment{ color rgb<1,0,0>} \n\
        finish {ambient 0.1 \n\
                 diffuse 0.9 \n\
                 phong 1}}\n'

    print 'camera { \n\
      location <sin(2*pi*clock)*'+str(2*fac)+','+str(0*fac)+', cos(2*pi*clock)*'+str(2*fac)+'>\n\
      look_at <0,0,0>\n\
      focal_point < 0, 0, 0> \n\
      aperture 0.8 \n\
      blur_samples 20 \n\
      confidence 0.9 \n\
      variance 1/128 \n\
     }\n'

    for x in range(3, 4):
        for y in range(3, 4):
            for z in range(3, 4):
                print 'light_source { \n\
                    <'+str(x*fac)+', '+str(y*fac)+', '+str(z*fac)+'> \n\
                    color rgb<1,1,1> \n\
                }\n'
    print 'light_source { \n\
                    <'+str(0*fac)+', '+str(5*fac)+', '+str(0*fac)+'> \n\
                    color rgb<1,1,1> \n\
                }\n'

    while True:
        try:
            line = raw_input()
            res = json.loads(line)
            s = 'sphere { '
            s += '<' + str(res['x']*fac) + ', ' + str(res['y']*fac) + ', ' + str(res['z']*fac) + '>, '+ str(0.005*fac) + "\n"
            if res['a']:
                s += 'texture {texa}'
            else:
                s += 'texture {tex}'
            s += "\n" + '}' + "\n"
            print s
        except:
            break
