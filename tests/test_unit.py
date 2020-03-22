import unittest


class ConverterTests(unittest.TestCase):

    def test_calculate_intersect_area(self):
        from midv500.utils import calculate_intersect_area
        # check if intersection area is calculated correctly

        # case 1
        bbox1 = [25, 32, 55, 62]
        bbox2 = [26, 62, 54, 75]
        intersect_area = calculate_intersect_area(bbox1, bbox2)
        self.assertEqual(intersect_area, 0)

        # case 2
        bbox1 = [25, 32, 55, 62]
        bbox2 = [26, 30, 54, 75]
        intersect_area = calculate_intersect_area(bbox1, bbox2)
        self.assertEqual(intersect_area, 840)

    def test_get_bbox_inside_image(self):
        from midv500.utils import get_bbox_inside_image
        # check if bbox inside image is calculated correctly

        # form bbox regions
        label_bbox = [-200, 500, 2500, 600]
        # form image regions
        image_xmin = 0
        image_xmax = 1920
        image_ymin = 0
        image_ymax = 1080
        image_bbox = [image_xmin, image_ymin, image_xmax, image_ymax]
        # calculate corrected regions
        corrected_label_bbox = get_bbox_inside_image(label_bbox, image_bbox)
        self.assertEqual(corrected_label_bbox, [0, 500, 1920, 600])

    def test_list_annotation_paths_recursively(self):
        from midv500.utils import list_annotation_paths_recursively
        # check if annotations paths can be read

        directory = "tests/test_data/data/"
        # read annotations paths
        annotation_paths = list_annotation_paths_recursively(directory, ignore_background_only_ones=True)
        self.assertEqual(len(annotation_paths), 90)

    def test_download(self):
        from midv500.utils import download
        # check if annotations paths can be read

        url = "https://github.com/fcakyon/midv500/raw/master/tests/test_data/CA43_01.zip"
        save_dir = "tests/test_data/"
        # read annotations paths
        download(url, save_dir)

    def test_unzip(self):
        from midv500.utils import unzip
        # check if annotations paths can be read

        file_path = "tests/test_data/CA43_01.zip"
        dest_dir = "tests/test_data/"
        # read annotations paths
        unzip(file_path, dest_dir)


if __name__ == '__main__':
    unittest.main()
