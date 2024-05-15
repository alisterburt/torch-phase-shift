import torch

from .phase_shift_grids import phase_shift_grid_2d, phase_shift_grid_3d


def phase_shift_dft_2d(
    dft: torch.Tensor,
    image_shape: tuple[int, int],
    shifts: torch.Tensor,
    rfft: bool,
    fftshifted: bool,
):
    """Apply phase shifts to 2D discrete Fourier transforms.

    Parameters
    ----------
    dft: torch.Tensor
        `(..., h, w)` array containing DFTs.
    image_shape: tuple[int, int]
        `(h, w)` of images prior to DFT computation.
    shifts: torch.Tensor
        `(..., 2)` array of 2D shifts in `h` and `w`.
    rfft: bool
        Whether the input was computed using `rfft`.
    fftshifted: bool
        Whether the DFTs have been fftshifted to center the DC component.

    Returns
    -------
    shifted_dfts: torch.Tensor
        `(..., h, w)` array of DFTs with phase shifts applied.
    """
    phase_shifts = phase_shift_grid_2d(
        shifts=shifts,
        image_shape=image_shape,
        rfft=rfft,
        fftshift=fftshifted,
    )
    return dft * phase_shifts


def phase_shift_dft_3d(
    dft: torch.Tensor,
    image_shape: tuple[int, int, int],
    shifts: torch.Tensor,
    rfft: bool = False,
    fftshifted: bool = False,
):
    """Apply phase shifts to 3D discrete Fourier transforms.

    Parameters
    ----------
    dft: torch.Tensor
        `(..., h, w)` array containing DFTs.
    image_shape: tuple[int, int, int]
        `(h, w)` of images prior to DFT computation.
    shifts: torch.Tensor
        `(..., 3)` array of 3D shifts in `d`, `h` and `w`.
    rfft: bool
        Whether the input was computed using `rfft`.
    fftshifted: bool
        Whether the DFTs have been fftshifted to center the DC component.

    Returns
    -------
    shifted_dfts: torch.Tensor
        `(..., h, w)` array of DFTs with phase shifts applied.
    """
    phase_shifts = phase_shift_grid_3d(
        shifts=shifts,
        image_shape=image_shape,
        rfft=rfft,
        fftshift=fftshifted,
    )
    return dft * phase_shifts
