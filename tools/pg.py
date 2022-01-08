import torch

def main():
    a = torch.randn(5)
    b = a**2 / a.norm(2)**2
    print(a, b, torch.sum(b))
    return None

if __name__ == '__main__':
    main()