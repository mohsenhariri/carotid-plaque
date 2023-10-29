import medviz as viz


print(viz.__version__)

mask = "dataset/air rt sinus+ cortical bone.nii.gz"

mask = viz.im2arr(mask)

print(mask.shape)