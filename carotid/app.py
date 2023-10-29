import medviz as viz

print(viz.__version__)

mask = "dataset/air rt sinus+ cortical bone.nii.gz"
image = "/storage/sync/git/mohsen/carotid-plaque/dataset/2-18-2021.dcm"

viz.plot3d(images=image, masks=mask)
