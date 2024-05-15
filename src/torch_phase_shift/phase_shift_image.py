import torch

from .phase_shift_dft import phase_shift_dft_2d, phase_shift_dft_3d


def phase_shift_image_2d(image: torch.Tensor, shifts: torch.Tensor):
    """Translate one or more 2D images by phase shifting their Fourier transforms.

    Parameters
    ----------
    image: torch.Tensor
        `(..., h, w)` image(s).
    shifts: torch.Tensor
        `(..., 2)` array of 2D shifts in `h` and `w`.

    Returns
    -------
    shifted_images: torch.Tensor
        `(..., h, w)` array of DFTs with phase shifts applied.
    """
    h, w = image.shape[-2:]
    image = torch.fft.rfftn(image, dim=(-2, -1))
    image = phase_shift_dft_2d(
        image,
        image_shape=(h, w),
        shifts=shifts,
        rfft=True,
        fftshifted=False
    )
    image = torch.fft.irfftn(image, dim=(-2, -1))
    return torch.real(image)


def phase_shift_image_3d(image: torch.Tensor, shifts: torch.Tensor):
    """Translate one or more 3D images by phase shifting their Fourier transforms.

    Parameters
    ----------
    image: torch.Tensor
        `(..., h, w)` image(s).
    shifts: torch.Tensor
        `(..., 3)` array of 2D shifts in `d`, `h` and `w`.

    Returns
    -------
    shifted_images: torch.Tensor
        `(..., d, h, w)` array of DFTs with phase shifts applied.
    """
    d, h, w = image.shape[-3:]
    image = torch.fft.rfftn(image, dim=(-3, -2, -1))
    image = phase_shift_dft_3d(
        image,
        image_shape=(d, h, w),
        shifts=shifts,
        rfft=True,
        fftshifted=False
    )
    image = torch.fft.irfftn(image, dim=(-3, -2, -1))
    return torch.real(image)
