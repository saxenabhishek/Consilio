"""

Demo on how to use Cppn 

"""

from Cppn import Cppn

if __name__ == "__main__":
    M = Cppn()
    r = M()

    # r is the image
    print("Simple call",r.shape)

    # change image size
    r = M(100,100)
    print("Modified call",r.shape)

    # to show image
    #plt.imshow(r)
    # plt.show() 