import bpy

def main():
    context = bpy.context
    rig_object = context.active_object
    for bone in rig_object.pose.bones:
        translate(bone)
        
def translate(bone):
    
    #LOC
    NEW_X_LOC=bone.location[1]*-1
    NEW_Y_LOC=bone.location[0]
    NEW_Z_LOC=bone.location[2]
    
	#ROT
	NEW_W_ROT=bone.rotation_quaternion[0]
    NEW_X_ROT=abs(bone.rotation_quaternion[2])*Xsign(bone.rotation_quaternion[1],bone.rotation_quaternion[2])
    NEW_Y_ROT=abs(bone.rotation_quaternion[1])*Ysign(bone.rotation_quaternion[1],bone.rotation_quaternion[2])
    NEW_Z_ROT=bone.rotation_quaternion[3]
    
    #SCA
    NEW_X_SCA=bone.scale[1]
    NEW_Y_SCA=bone.scale[0]
    NEW_Z_SCA=bone.scale[2]
	
    
    
    bone.location[0]=NEW_X_LOC
    bone.location[1]=NEW_Y_LOC
    bone.location[2]=NEW_Z_LOC
    
    bone.rotation_quaternion[0]=NEW_W_ROT
    bone.rotation_quaternion[1]=NEW_X_ROT
    bone.rotation_quaternion[2]=NEW_Y_ROT
    bone.rotation_quaternion[3]=NEW_Z_ROT
    
    bone.scale[0]=NEW_X_SCA
    bone.scale[1]=NEW_Y_SCA
    bone.scale[2]=NEW_Z_SCA
    
def Xsign(x, y):
    if(x>0 and y>0):
        return -1
    if(x<0 and y<0):
        return 1      
    if(x>0 and y<0):
        return 1  
    if(x<0 and y>0):
        return -1      
    return 1
        
def Ysign(x, y):
    if(x>0 and y>0):
        return 1
    if(x<0 and y<0):
        return -1      
    if(x>0 and y<0):
        return 1  
    if(x<0 and y>0):
        return -1      
    return 1
    
main()