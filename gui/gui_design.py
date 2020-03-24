import sys, json


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from loguru import logger
from gui.stash_design import Ui_MainWindow
import stash
import item_treatment
import filter


# TODO: Habilitar criação e escolha de filtros
from gui.worker_qt import Worker


class StashDesign(QMainWindow, Ui_MainWindow):
    FilterLoaded = pyqtSignal()
    def __init__(self):
        QMainWindow.__init__(self)

    def setupUi(self, MainWindow):
        super(StashDesign, self).setupUi(MainWindow)
        self.poesessid_text = ''
        self.poetabs_text = ''
        self.json_text = ''
        self.filters = {}
        self.GetStashButton.clicked.connect(self.stash_worker)
        self.ImportFiltersButton.clicked.connect(self.filter_worker)
        self.FilterLoaded.connect(self.load_filters_combobox)
        self.SelectFilterCombo.currentTextChanged.connect(self.change_filter_description)

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())



    @property
    def stash_tabs(self):
        return self._stash_tabs

    @stash_tabs.setter
    def stash_tabs(self, value):
        self._stash_tabs = value

    @property
    def stash_items(self):
        return self._stash_tabs

    @stash_items.setter
    def stash_items(self, value):
        self._stash_items = value

    def progress_fn(self, n):
        print("%d%% done" % n)

    def stash_execute_fn(self, progress_callback):
        return self.get_text_inputs()

    def filter_execute_fn(self, progress_callback):
        return self.get_filters()

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def filter_worker(self):
        # Pass the function to execute
        # Any other args, kwargs are passed to the run function
        worker = Worker(self.filter_execute_fn)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def stash_worker(self):
        # Pass the function to execute
        worker = Worker(self.stash_execute_fn)  # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)
        self.stackedWidget.setCurrentIndex(1)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)

    def get_text_inputs(self):
        self.poesessid_text = self.input_poesessid.toPlainText()
        logger.debug(self.poesessid_text)
        self.poetabs_text = self.input_poetabs.toPlainText()
        self.poetabs_text = self.poetabs_text.split(',')
        logger.debug(self.poetabs_text)
        logger.debug('Downloading stash')
        self.stash_tabs = stash.get_account_tabs(self.poesessid_text, self.poetabs_text)
        logger.debug('Stash tabs downloaded')
        logger.debug('Reading items')
        self.stash_items = item_treatment.get_items_from_all_tabs(self.stash_tabs)

    def get_filters(self):
        # filename, _ = QFileDialog.getOpenFileName(self, 'Open file', '../')
        self.filters = filter.open_filters_files('../filters.json')
        logger.debug(self.filters)
        self.FilterLoaded.emit()

    def load_filters_combobox(self):
        logger.debug('Loading filters combobox')
        for filter_name in self.filters.keys():
            logger.debug(filter_name)
            self.SelectFilterCombo.addItem(filter_name)

    def change_filter_description(self, filter_name):
        self.ShowFilterStatsText.setText(json.dumps(self.filters[filter_name], indent=4))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = StashDesign()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())